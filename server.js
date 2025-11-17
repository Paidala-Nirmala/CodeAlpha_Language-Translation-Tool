const express = require('express');
const cors = require('cors');
const axios = require('axios');
require('dotenv').config();

const app = express();
app.use(cors());
app.use(express.json());

const GOOGLE_API_KEY = process.env.GOOGLE_API_KEY;

// Translation endpoint
app.post('/api/translate', async (req, res) => {
  const { text, source, target } = req.body;
  try {
    const response = await axios.post(
      `https://translation.googleapis.com/language/translate/v2?key=${GOOGLE_API_KEY}`,
      {
        q: text,
        source: source,
        target: target,
        format: 'text',
      }
    );
    res.json(response.data);
  } catch (error) {
    res.status(500).json({ error: 'Translation failed.' });
  }
});

const PORT = process.env.PORT || 5000;
app.listen(PORT, () => console.log(`Server running on port ${PORT}`));
