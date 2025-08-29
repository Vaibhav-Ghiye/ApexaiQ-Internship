const express = require('express');
const fs = require('fs');
const path = require('path');

const app = express();
app.use(express.json()); // to handle JSON body

const File = path.join(__dirname, 'notes.json');

// Ensure file exists
if (!fs.existsSync(File)) {
  fs.writeFileSync(File, JSON.stringify([]));
}

// Route 1: Get all notes
app.get('/notes', (req, res) => {
  const notes = JSON.parse(fs.readFileSync(File));
  res.json(notes);
});

// Route 2: Add a new note
app.post('/notes', (req, res) => {
  const notes = JSON.parse(fs.readFileSync(File));

  const newNote = { id: Date.now(), text: req.body.text };
  notes.push(newNote);
  
  fs.writeFileSync(File, JSON.stringify(notes, null, 2));
  res.status(201).json(newNote);
});

const PORT = 3000;
app.listen(PORT, () => {
  console.log(`Server running on http://localhost:${PORT}`);
});
