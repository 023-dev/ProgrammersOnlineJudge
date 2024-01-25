-- 코드를 입력하세요
SELECT 
    T1.REST_ID
    , T1.REST_NAME
    , T1.FOOD_TYPE
    , T1.FAVORITES
    , T1.ADDRESS
    , T2.SCORE
FROM
    REST_INFO T1
     JOIN (
        SELECT
            REST_ID
            , ROUND(AVG(REVIEW_SCORE), 2) AS SCORE
        FROM
            REST_REVIEW
        GROUP BY REST_ID
    ) T2
    ON T1.REST_ID = T2.REST_ID
WHERE 1 = 1
    AND T1.ADDRESS LIKE '서울%'    
ORDER BY
    T2.SCORE DESC
    , T1.VIEWS DESC