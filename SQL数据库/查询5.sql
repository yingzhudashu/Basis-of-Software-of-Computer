SELECT SCORE.CNO,CNAME,ƽ����=AVG(DEGREE)
FROM COURSE,SCORE
WHERE SCORE.CNO=COURSE.CNO
GROUP BY SCORE.CNO,CNAME
ORDER BY AVG(DEGREE)DESC