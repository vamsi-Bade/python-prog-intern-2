def word_count(sentence):
    """
    Function to count the number of words in a sentence or paragraph.
    
    Args:
    sentence (str): The input sentence or paragraph.
    
    Returns:
    int: The count of words in the input.
    """
    # Split the sentence by whitespace to count words
    words = sentence.split()
    return len(words)

def main():
    # Prompt the user to enter a sentence or paragraph
    user_input = input("Enter a sentence or paragraph: ")
    
    # Check for empty input
    if not user_input.strip():
        print("Error: Empty input. Please enter a sentence or paragraph.")
        return
    
    # Count the words in the input
    count = word_count(user_input)
    
    # Display the word count
    print("Word count:", count)

if __name__ == "__main__":
    main()
