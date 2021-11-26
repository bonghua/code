SELECT 水质类别,round( 100.0*数量/138,2) || '%' 百分比
--FROM(
--SELECT sum(数量)
FROM (SELECT 水质类别 ,count(*) 数量 
FROM water
WHERE not 叶绿素 ='*' 
GROUP BY 水质类别
--HAVING 水质类别 IN('劣Ⅴ','Ⅴ','Ⅰ')
ORDER BY 数量)
--)
 