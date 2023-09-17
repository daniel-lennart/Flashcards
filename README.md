# Flashcard Generator from Document

This Streamlit app allows users to generate flashcards from a given document using the power of GPT and Langchain. By analyzing the content of the document, the app identifies key concepts, definitions, and other important information to suggest potential flashcards.

## Functionality

1. **Document Input**: Users can paste their document text into a textbox
2. **Analysis**: After pasting the text, users can click a button to send the input to GPT for analysis.
3. **Summary & Suggestions**: The app will then display a summary of the text with all suggestions for flashcards highlighted.

## Rules for Creating Flashcards

Flashcards are generated based on the following criteria:

1. **Definitions**: Any sentence that defines a term or concept is a candidate for a flashcard. For example, "Photosynthesis is the process by which green plants and some other organisms use sunlight to synthesize foods."
2. **Main Concepts**: Key concepts or topics that are central to the document's theme or subject.
3. **Important Dates**: Any historical or significant dates mentioned in the document.
4. **Formulas**: In case of scientific or mathematical documents, any formula is a candidate.
5. **Contrasts or Comparisons**: Sentences that contrast or compare two or more things can be turned into a flashcard. For example, "Unlike mammals, birds lay eggs."
6. **Lists**: Any enumerated list or series of related items can be a candidate, especially if they detail steps, types, or categories.

## How to Use

1. Paste your document text into the provided textbox.
2. Click the "Analyze" button.
3. Review the summary and highlighted suggestions for flashcards.
4. Use the suggestions to create flashcards in Obsidian or any other flashcard tool.

## Future Enhancements

- Generating .md file for Obsidian flash cards
- pdf, .md, docx and powerpoint file support
- Option to customize the rules for flashcard generation based on user preference.

