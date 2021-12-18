SELECT hh.姓名,是否优秀
FROM  hh LEFT JOIN
(SELECT 姓名,iif(成绩>90,'是',NULL) 是否优秀
FROM hh) new 
ON hh.姓名=new.姓名 
ORDER BY 成绩 DESC