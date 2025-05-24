const express = require('express');
const cors = require('cors');
const sqlite3 = require('sqlite3').verbose();
const nodemailer = require('nodemailer');

const app = express();
const PORT = 5000;

// Подключение и создание базы данных
const db = new sqlite3.Database('./database.db', (err) => {
  if (err) {
    console.error("Ошибка подключения к базе данных:", err.message);
  } else {
    console.log("Подключение к базе данных успешно!");
  }
});

// Создаем таблицу, если ее нет
db.run(`
  CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    company TEXT,
    email TEXT UNIQUE
  )
`);

app.use(express.json());
app.use(cors());

// Настройка почтового транспорта (замените данные на свои)
const transporter = nodemailer.createTransport({
  service: 'gmail',
  auth: {
    user: 'your-email@gmail.com',       // замените на ваш email
    pass: 'your-email-password'           // замените на ваш пароль или app password
  }
});

// Обработчик отправки формы
app.post('/submit', (req, res) => {
  const { company, email } = req.body;

  // Проверяем, есть ли уже такая запись
  db.get("SELECT * FROM users WHERE email = ? OR company = ?", [email, company], (err, row) => {
    if (err) {
      return res.status(500).json({ message: "Ошибка базы данных" });
    }
    if (row) {
      return res.json({ message: "Вы уже в списке :)" });
    } else {
      // Вставляем данные в базу
      db.run("INSERT INTO users (company, email) VALUES (?, ?)", [company, email], function(err) {
        if (err) {
          return res.status(500).json({ message: "Ошибка базы данных при вставке" });
        }
        
        // Отправляем email с уведомлением
        const mailOptions = {
          from: 'your-email@gmail.com',
          to: 'receiver@example.com',  // замените на адрес, куда нужно отправлять данные
          subject: 'Новая заявка',
          text: `Компания: ${company}\nEmail: ${email}`
        };

        transporter.sendMail(mailOptions, (error, info) => {
          if (error) {
            console.error("Ошибка отправки почты:", error);
            return res.status(500).json({ message: "Ошибка отправки почты" });
          }
          res.json({ message: "Данные успешно отправлены!" });
        });
      });
    }
  });
});

app.listen(PORT, () => {
  console.log(`Сервер запущен на порту ${PORT}`);
});
