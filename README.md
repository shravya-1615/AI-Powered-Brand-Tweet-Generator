# AI Brand Tweet Generator

A complete end-to-end AI-powered web app that generates 10 on-brand tweets based on brand inputs.

## Features

- Streamlit frontend for brand input
- Brand voice analysis via `utils/brand_analysis.py`
- Prompt building via `utils/prompt_templates.py`
- OpenAI text generation with fallback mock data in `utils/tweet_generator.py`
- Tweet list output with download and copy support
- Simple, modular code and clean error handling

## Project Structure

```
ai_tweet_generator/
│
├── app.py
├── requirements.txt
├── README.md
│
├── utils/
│   ├── brand_analysis.py
│   ├── tweet_generator.py
│   └── prompt_templates.py
│
└── data/
    └── sample_brands.json
```

## Installation

1. Clone or copy files into your local workspace.
2. Create a virtual environment:

```bash
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # macOS/Linux
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. (Optional) Add your OpenAI API key in `.env`:

```
OPENAI_API_KEY=your_openai_key
OPENAI_ENGINE=text-davinci-003
```

## Run

```bash
streamlit run app.py
```

## Usage

- Enter brand name, industry, campaign objective, description.
- Click `Generate Tweets`.
- View brand voice summary and generated tweets.
- Download `.txt` or copy manually.

## Notes

- If OpenAI API key is missing or fails, the app returns mock tweets.
- Each generated tweet is limited to 280 characters.
