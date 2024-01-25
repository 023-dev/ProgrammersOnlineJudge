SELECT 
    *
FROM
    (
    SELECT 
        ANIMAL_TYPE
        , COUNT(ANIMAL_TYPE) 
    FROM 
        ANIMAL_INS 
    GROUP BY 
        ANIMAL_TYPE
    ) T
ORDER BY 
    T.ANIMAL_TYPE ASC