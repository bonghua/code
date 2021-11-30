SELECT 数据来源,count(新闻标题) 各新闻来源新闻数 
FROM gitnew9
WHERE 创造时间>'2021-11-28 00:08:00' AND 发布时间<'2021-11-28 00:20:00'
GROUP BY 数据来源
ORDER BY 各新闻来源新闻数 DESC
--LIMIT 10