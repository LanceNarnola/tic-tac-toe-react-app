const express = require('express');
const http = require('http');
const { Server } = require('socket.io');
const app = express();
const server = http.createServer(app);
const io = new Server(server);

app.use(express.static('public')); // To serve the React app

// Handle socket connections
io.on('connection', (socket) => {
  console.log('A user connected');
  
  socket.on('move', (data) => {
    io.emit('move', data); // Broadcast move to all clients
  });

  socket.on('disconnect', () => {
    console.log('A user disconnected');
  });
});

server.listen(3001, () => {
  console.log('Server is running on port 3001');
});