-- PostgreSQL
SELECT *
FROM admissions
WHERE patient_id = 542
GROUP BY patient_id, admission_date, discharge_date, diagnosis, attending_doctor_id
HAVING admission_date = MAX(admission_date);

-- sql
SELECT *
FROM admissions
WHERE patient_id = 542
ORDER BY admission_date DESC
LIMIT 1;