const express = require('express');
const fs = require('fs');
const path = require('path');
require('dotenv').config();

const app = express();
app.use(express.json()); 

const notesFile = path.join(__dirname, 'notes.json');

// Check if file exists
if (!fs.existsSync(notesFile)) {
  fs.writeFileSync(notesFile, JSON.stringify([]));
}

// Get all notes
app.get('/notes', (req, res) => {
  const notes = JSON.parse(fs.readFileSync(notesFile));
  res.json(notes);
});

//  Add a new note
app.post('/notes', (req, res) => {
  const notes = JSON.parse(fs.readFileSync(notesFile));
  const newNote = { id: Date.now(), text: req.body.text };
  notes.push(newNote);
  fs.writeFileSync(notesFile, JSON.stringify(notes, null, 2));
  res.status(201).json(newNote);
});

const PORT = process.env.PORT || 5000;
app.listen(PORT, () => {
  console.log(`Server running on http://localhost:${PORT}`);
});
