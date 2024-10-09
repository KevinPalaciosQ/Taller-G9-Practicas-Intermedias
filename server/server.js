const express = require('express');
const bodyParser = require('body-parser');
const cors = require('cors');
const fs = require('fs');

const app = express();
const host = '127.0.0.1';
const port = 3001;


app.use(cors());
app.use(bodyParser.json());

const loadUsers = () => {
  if (fs.existsSync('users.json')) {
    const data = fs.readFileSync('users.json', 'utf8');
    return JSON.parse(data);
  }
  return [];
};

const saveUsers = (users) => {
  fs.writeFileSync('users.json', JSON.stringify(users, null, 2));
};

app.get('/', (req, res) => {
    res.send('Taller, introduccion a rasberry pi');
});

app.post('/register', (req, res) => {
  const users = loadUsers();
  const { username, password } = req.body;

  if (users.find(user => user.username === username)) {
    return res.status(400).json({ message: 'El usuario ya existe' });
  }

  users.push({ username, password });
  saveUsers(users);

  res.json({ message: 'Usuario registrado exitosamente' });
});

app.post('/login', (req, res) => {
  const users = loadUsers();
  const { username, password } = req.body;

  const user = users.find(user => user.username === username && user.password === password);

  if (!user) {
    return res.status(401).json({ message: 'Credenciales incorrectas' });
  }

  res.json({ message: 'Login exitoso' });
});

app.listen(port, host, () => {
    console.log(`Server running at http://${host}:${port}/`);
});