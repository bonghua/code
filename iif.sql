SELECT 
round(avg(成绩),2) 各成绩分等平均成绩,
iif(成绩>90 ,'90分以上',iif(成绩 BETWEEN 80 AND 90,'80-90',
iif(成绩 BETWEEN 70 AND 80,'70-80',
iif(成绩 BETWEEN 60 AND 70,'60-70',
iif(成绩 <60,'不及格',NULL ))))) 成绩分等
FROM hh
GROUP BY 成绩分等