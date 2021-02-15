-- Для каждой позиции чека 117-ого магазина (TxSaleLineItem) попробуй вывести подробную информацию о товаре (item). Чтобы соединить таблицы используй поле szitemid.

SELECT t.*, i.*

FROM tpnet_tpnsql00117_tpcentraldb_ods.v_txsalelineitem t

    LEFT JOIN tpnet_tpnsql00117_tpcentraldb_ods.v_item i 

    ON t.szitemid = i.szitemid

WHERE t.is_actual = '1' AND i.is_actual = '1'


-- На какую общую сумму были использованы подарочные карты в 117 магазине в период с 2020-01-01 по 2020-06-01. Результирующее число преобразовать к целому типу.


SELECT CAST(SUM(dAmount) AS int) 

FROM tpnet_tpnsql00117_tpcentraldb_ods.v_txlm_giftcard 

WHERE szdate::date BETWEEN '2020-01-01' AND '2020-06-01'

    AND is_actual = '1' ;
    
    
    
    
-- Сколько товаров из отдела 7.755.30.10 (item) ни разу не были проданы (TxSaleLineItem) в 117-ом магазине?
-- Запрос с EXCEPT (MINUS):
SELECT COUNT(*)

FROM (
         SELECT szitemid

         FROM tpnet_tpnsql00117_tpcentraldb_ods.v_item

         WHERE is_actual = '1'

           AND szposdepartmentid = '7.755.30.10'
             EXCEPT


         SELECT szitemid

         FROM tpnet_tpnsql00117_tpcentraldb_ods.v_txsalelineitem

         WHERE is_actual = '1'

           AND szposdepartmentid = '7.755.30.10'
     ) tmp


-- Посчитать количество чеков на каждый день с 2020-04-01 до 2020-05-01 в 117-ом магазине, пробитых на одиннадцатой кассе.



SELECT generate_series, COALESCE(tmp.cnt, 0)

FROM generate_series('2020-04-01'::date, '2020-05-01'::date, '1 day') LEFT JOIN (

    SELECT szdate, COUNT(*) AS cnt
    FROM tpnet_tpnsql00117_tpcentraldb_ods.v_txfooter
    WHERE szdate BETWEEN '2020-04-01' AND '2020-05-01'
    AND lworkstationnmbr = '11'
    AND is_actual = '1'
    GROUP BY szdate

    ) tmp
ON generate_series::date = tmp.szdate::date;

--     объединить заголовки чеков со строками чеков для 117 магазина в период с 2020-01-01 по 2020-06-01. Для каждой позиции чека в случае, если время закрытия всего чека больше 18:00, а количество единиц товара в конкретной строке чека больше 10, то в поле flag вывести 1, в противном случае – 0. Для каждой выделенной категории посчитать количество принадлежащих ей строк чеков.
--     Запрос с использованием CASE :
SELECT flag, COUNT(*)

FROM (
         SELECT tf.szdate::date,
                tf.sztime::time,
                sli.szdesc,
                sli.dTaQty,

                CASE
                    WHEN tf.sztime::time >= '18:00:00'
                        AND sli.dTaQty > 10 THEN 0

                    ELSE 1 END AS flag

         FROM tpnet_tpnsql00117_tpcentraldb_ods.v_txfooter AS tf

                  INNER JOIN tpnet_tpnsql00117_tpcentraldb_ods.v_txsalelineitem AS sli
                             ON tf.lretailstoreid = sli.lretailstoreid
                                 AND tf.lworkstationnmbr = sli.lworkstationnmbr
                                 AND tf.szdate = sli.szdate
                                 AND tf.sztime = sli.sztime
                                 AND tf.ltanmbr = sli.ltanmbr

         WHERE tf.szdate::date BETWEEN '2020-01-01'
                   AND '2020-06-01'
     ) tmp

GROUP BY flag;


-- Посчитать количество чеков на каждый день с 2020-04-01 до 2020-05-01 в 117-ом магазине, пробитых на одиннадцатой кассе.


SELECT generate_series, COALESCE(tmp.cnt, 0)
FROM generate_series('2020-04-01'::date, '2020-05-01'::date, '1 day')
         LEFT JOIN (
                    SELECT szdate, COUNT(*) AS cnt
                    FROM tpnet_tpnsql00117_tpcentraldb_ods.v_txfooter
                    WHERE szdate BETWEEN '2020-04-01' AND '2020-05-01'
                      AND lworkstationnmbr = '11'
                      AND is_actual = '1'
                    GROUP BY szdate
                    ) tmp ON generate_series::date = tmp.szdate::date

SELECT szitemid AS ID, szposdepartmentid AS pID
FROM sandbox_sql_course.test_4_item
WHERE is_actual = '1'
  AND pID = '7.755.30.10'