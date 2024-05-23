CREATE DATABASE IF NOT EXISTS medportal;
USE medportal;

CREATE TABLE IF NOT EXISTS medportal.Departments (
	id INTEGER AUTO_INCREMENT,
    name VARCHAR(50) NOT NULL,
    location VARCHAR(50) NOT NULL,
    PRIMARY KEY (id)
);


INSERT INTO medportal.Departments
    (name, location)
VALUES
    ('Приёмное отделение', 'Главный корпус'),
    ('Травматология', 'Главный корпус'),
    ('Хирургическое отделение', 'Корпус №2'),
    ('Кардиологическое отделение', 'Главный корпус'),
    ('Терапевтическое отделение', 'Главный корпус'),
    ('Педиатрическое отделение', 'Корпус №3'),
    ('Неврологическое отделение', 'Главный корпус'),
    ('Лаборатория', 'Корпус №1');


CREATE TABLE IF NOT EXISTS medportal.Medicines (
	id INTEGER AUTO_INCREMENT,
    name VARCHAR(150) NOT NULL,
    code CHAR(15) NOT NULL, 
    PRIMARY KEY (id)
);

INSERT INTO medportal.Medicines
    (name, code)
VALUES
    ("Олидетрим 2000 капсулы мягк. желат. по 2000 МЕ №60 (15х4)", '11111'),
    ("Аквадетрим витамин D3 раствор д/перор. прим., вод. 15000 МЕ/мл по 10 мл", '22222'),
	("Магний активный таблетки по 0,5 г №80", '33333'),
	("Омега-3 1000 мг капсулы №30 Ronpharm", '44444'),
	("Анальгин-Дарница таблетки по 500 мг №10", '55555'),
    ("Нимесил гранулы д/ор. сусп. 100 мг/2 г по 2 г №30 (3х10) в пак.", 'AA123'),
	("Парацетамол-Дарница таблетки по 500 мг №10", 'Ab265'),
	("Ибупрофен таблетки, п/о по 200 мг №50 (10х5)", 'LK61R'),
	("Диклофенак гель 5 % по 50 г в тубах", '999GH'),
    ("Цетрин таблетки, п/плен. обол. по 10 мг №20 (10х2)", '265RF'),
	("Декатилен таблетки д/рассас. №20 (10х2)", 'MS987'),
	("Спазмалгон таблетки №20 (10х2)", 'AS123'),
	("Но-шпа таблетки по 40 мг №24 (24х1)", '87882'),
    ("Мукалтин форте с витамином С таблетки д/жев. №20 (10х2)", '01012'),
	("Супрадин Актив таблетки, п/плен. обол. №30 во флак.", 'LS54D'),
	("L-тироксин 100 Берлин-Хеми таблетки по 100 мкг №50 (25х2)", '26262'),
	("Эргоферон таблетки №20", 'JS898');


CREATE TABLE IF NOT EXISTS medportal.Positions (
	id INTEGER AUTO_INCREMENT,
	name VARCHAR(50) NOT NULL,
    PRIMARY KEY (id),
    UNIQUE (name)
);

INSERT INTO medportal.Positions
    (name)
VALUES
   ('Врач-невролог'),
   ('Врач-аллерголог'),
   ('Врач-анестезиолог'),
   ('Врач-гастроэнтеролог'),
   ('Врач-гематолог'),
   ('Врач-эндоскопист'),
   ('Врач-иммунолог'),
   ('Врач-кардиолог'),
   ('Врач-хирург'),
   ('Врач-травматолог'),
   ('Врач-рентгенолог'),
   ('Врач-терапевт'),
   ('Медицинская сестра'),
   ('Заведующий отделением');
   

CREATE TABLE IF NOT EXISTS medportal.Doctors (
	id INTEGER AUTO_INCREMENT,
	name VARCHAR(50) NOT NULL,
    surname VARCHAR(100) NOT NULL,
    phone CHAR(15) NOT NULL,
    email VARCHAR(100) NOT NULL,
    password VARCHAR NOT NULL, 
    department_id INTEGER NOT NULL,
    position_id INTEGER NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (department_id) REFERENCES Departments(id),
    FOREIGN KEY (position_id) REFERENCES Positions(id)
);


CREATE TABLE IF NOT EXISTS medportal.Patients (
	id INTEGER AUTO_INCREMENT,
	name VARCHAR(50) NOT NULL,
    surname VARCHAR(100) NOT NULL,
    phone CHAR(15) NOT NULL,
    gender ENUM('Женский пол', 'Мужской пол') NOT NULL,
    date_of_birth DATE NOT NULL,
    PRIMARY KEY (id)
);


CREATE TABLE IF NOT EXISTS medportal.Consultations (
	id INTEGER AUTO_INCREMENT,
    patient_id INTEGER NOT NULL,
    doctor_id INTEGER NOT NULL,
    complaint TEXT NOT NULL,
    diagnosis TEXT NOT NULL,
    date DATE NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (patient_id) REFERENCES Patients (id),
    FOREIGN KEY (doctor_id) REFERENCES Doctors (id)
);
    

CREATE TABLE IF NOT EXISTS medportal.PatientsSchemas (
	id INTEGER AUTO_INCREMENT,
    medicine_id INTEGER,
    consultation_id INTEGER NOT NULL,
    description TEXT NOT NULL,
    start_date DATE NOT NULL,
	end_date DATE NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (medicine_id) REFERENCES Medicines (id),
    FOREIGN KEY (consultation_id) REFERENCES Consultations (id)
);


