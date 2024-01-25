-- 코드를 입력하세요
SELECT 
    PRICE AS MAX_PRICE 
FROM PRODUCT 
WHERE 1 = 1
    AND PRICE = (
        SELECT 
            MAX(PRICE) 
        FROM PRODUCT
    )