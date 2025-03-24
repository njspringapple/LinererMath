# 定义
v_numeric <- c(1, 2, 3, 4, 5)
v_charactor <- c("a", "b", "c", "d", "e")
v_logical <- c(TRUE, FALSE, TRUE, FALSE, TRUE)
print(v_numeric)

# 向量的长度
length(v_numeric)

# 向量的加法 - 图形上的意义是向量的平移
v <- c(1, 2)
w <- c(3, 4)
v + w # 结果为 4 6

# 标量与向量的运算 - 图形上的意义是向量的平移
v + 1 # 结果为 2 3
v * 2 # 结果为 2 4

# 向量的线性组合
a <- 2
b <- 3
a * v + b * w # 结果为 11 16

v <- c(1, 2, 3)
w <- c(4, 5, 6)
u <- c(7, 8, 9)
a <- 2
b <- 3
c <- 4
a * v + b * w + c * u # 结果为 30 36 42

library(httr)
library(jsonlite)
library(ggplot2)
library(dplyr)
library(scales)
library(patchwork)

library(lubridate)

api_url <- "https://dcst.bjdcjtjt.com/getslotseizuredata"

payload <- list(parkid = "PCPXtcXRpXBSwykTwaWjKtFw")

response <- POST(
    url = api_url,
    body = toJSON(payload, auto_unbox = TRUE),
    content_type("application/json"),
    encode = "json"
)

if (status_code(response) == 200) {
    # 解析响应内容
    data <- fromJSON(content(response, "text", encoding = "UTF-8"))

    # 转换为数据框(假设返回的是JSON数组)
    df <- as.data.frame(data)

    # 每天一张图
    # 设置实际车位容量
    actual_capacity <- 59
    slotseizesequence <- df
    slotseizesequence$time_point <- as.POSIXct(paste(df$date, df$time))

    # 拆分时间好绘图
    slotseizesequence <- slotseizesequence %>%
        mutate(
            date = as.Date(time_point),
            hour = hour(time_point),
            minute = minute(time_point),
            count = ifelse(count > count, actual_capacity, count),
            is_weekend = ifelse(lubridate::wday(date) %in% c(1, 7), "周末", "工作日")
        )

    # 为数据添加小时列，时间段分类和占用率计算
    slotseizesequence <- slotseizesequence %>%
        filter(date >= "2025-03-08" & date <= "2025-03-25") %>%
        mutate(
            hour_of_day = hour(time_point) + minute(time_point) / 60,
            occupancy_rate = count / actual_capacity * 100, # 计算占用率百分比
            # 添加时段分类
            time_period = cut(
                hour_of_day,
                breaks = c(0, 6, 12, 18, 24),
                labels = c("凌晨", "上午", "下午", "晚上"),
                include.lowest = TRUE
            )
        )

    # 为每个日期和时段计算平均占用率，用于添加标签
    period_avg <- slotseizesequence %>%
        group_by(date, time_period) %>%
        summarise(
            avg_count = mean(count, na.rm = TRUE),
            avg_rate = mean(occupancy_rate, na.rm = TRUE),
            mid_hour = mean(range(hour_of_day)), # 计算时段中间点，用于放置标签
            .groups = "drop"
        )

    # 创建自定义渐变色方案
    gradient_colors <- list(
        "凌晨" = scale_fill_gradient(low = "#081d58", high = "#1d91c0", guide = "none"),
        "上午" = scale_fill_gradient(low = "#ffffd9", high = "#fdbb84", guide = "none"),
        "下午" = scale_fill_gradient(low = "#fcbba1", high = "#a50f15", guide = "none"),
        "晚上" = scale_fill_gradient(low = "#54278f", high = "#08306b", guide = "none")
    )

    # 创建带有时段填充和占用率标签的时间序列图
    ggplot(slotseizesequence, aes(x = hour_of_day, y = count)) +
        # 使用时段作为填充色
        geom_area(aes(fill = time_period), alpha = 0.85) +

        # 添加轮廓线
        geom_line(color = "black", linewidth = 0.4, alpha = 0.7) +

        # 添加实际车位容量线
        geom_hline(
            yintercept = actual_capacity,
            linetype = "dashed",
            color = "#2E8B57",
            linewidth = 0.8
        ) +

        # 添加工作日/周末平滑趋势线
        geom_smooth(aes(color = is_weekend, group = interaction(is_weekend, date)),
            method = "loess", span = 0.3,
            linewidth = 1, se = FALSE, alpha = 0.8
        ) +

        # 添加白色反色占用率标签
        geom_label(
            data = period_avg,
            aes(
                x = mid_hour,
                y = avg_count,
                label = sprintf("%.1f%%", avg_rate),
                fill = time_period
            ),
            color = "white",
            fontface = "bold",
            size = 3,
            label.padding = unit(0.15, "lines"),
            label.r = unit(0.15, "lines"),
            show.legend = FALSE
        ) +

        # 按日期分面
        facet_wrap(~date, scales = "free_y", ncol = 3) +

        # 设置填充色 - 使用时间段的分类颜色
        scale_fill_manual(
            values = c(
                "凌晨" = "#2171b5",
                "上午" = "#fecc5c",
                "下午" = "#fd8d3c",
                "晚上" = "#7a0177"
            ),
            name = "时间段"
        ) +

        # 设置坐标轴和标签
        scale_x_continuous(
            breaks = c(0, 6, 12, 18, 24),
            labels = c("00:00", "06:00", "12:00", "18:00", "24:00"),
            expand = expansion(mult = c(0.01, 0.01))
        ) +
        scale_y_continuous(
            labels = scales::comma,
            expand = expansion(mult = c(0, 0.1)),
            # 添加占用率次坐标轴
            sec.axis = sec_axis(
                ~ . / actual_capacity * 100,
                name = "车位占用率 (%)",
                breaks = seq(0, 100, 25)
            )
        ) +
        scale_color_manual(
            values = c("工作日" = "black", "周末" = "darkred"),
            labels = c("工作日", "周末"),
            name = "趋势线"
        ) +

        # 设置主题
        theme_minimal() +
        theme(
            legend.position = "bottom",
            legend.box = "vertical",
            legend.title = element_text(size = 9),
            legend.text = element_text(size = 8),
            panel.grid.minor = element_blank(),
            strip.text = element_text(size = 9, face = "bold"),
            strip.background = element_rect(fill = "lightyellow", color = NA),
            axis.title.x = element_text(size = 9),
            plot.title = element_text(hjust = 0.5, face = "bold"),
            plot.subtitle = element_text(hjust = 0.5, size = 9),
            # 设置次坐标轴文本颜色
            axis.title.y.right = element_text(color = "#2E8B57"),
            axis.text.y.right = element_text(color = "#2E8B57"),
            # 调整分面间距
            panel.spacing = unit(0.8, "lines")
        ) +

        # 添加标题和标签
        labs(
            title = "交道口车位占用时间变化及平均占用率",
            subtitle = paste(
                "数据时间范围:", format(min(slotseizesequence$time_point), "%Y-%m-%d"),
                "至", format(max(slotseizesequence$time_point), "%Y-%m-%d"),
                "| 实际车位: 52个 | 总体平均占用率:",
                sprintf("%.1f%%", mean(slotseizesequence$count, na.rm = TRUE) / actual_capacity * 100)
            ),
            x = "小时",
            y = "占用车位数"
        )
} else {
    cat("请求失败，状态码:", status_code(response))
}
