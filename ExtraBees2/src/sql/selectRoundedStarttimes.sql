SELECT ID, parsedDate, DATE_SUB(DATE_FORMAT(parsedDate, "%Y-%m-%d %H:%i:00"), INTERVAL MINUTE(parsedDate) % 5 MINUTE) FROM datavis.networkflow LIMIT 3000, 5000;