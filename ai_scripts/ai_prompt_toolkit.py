"""
AI Prompt Toolkit — QA Test Case Generator
===========================================
How to use:
1. Copy your story details (description, acceptance criteria, tech stack)
2. Paste them into the `feature` variable below (use triple quotes for multi-line)
3. Run: python ai_scripts/ai_prompt_toolkit.py
4. Copy the output and paste it into Claude.ai
5. Review the generated test cases and refine based on your domain knowledge

Tips:
- The more context you provide, the better the test cases
- Always include acceptance criteria if available
- Add tech stack details to get more relevant edge cases
"""

# This function takes a feature description and builds a structured AI prompt
def generate_test_case_prompt(feature_description):
    # Build the prompt template using the feature description
    prompt = f"""
You are a Senior QA Engineer with 13+ years of experience.

Given the following feature description:
"{feature_description}"

Generate 10 test cases covering:
- Happy path scenarios
- Negative scenarios
- Edge cases
- Integration points
- Performance considerations

For each test case provide:
- Test case name
- Preconditions
- Steps
- Expected result
"""
    return prompt  # Return the formatted prompt


# This block runs only when the script is executed directly
if __name__ == "__main__":
    # Define the feature you want to generate test cases for
    feature = """
    Feature: Add to Cart
    Description: As a user, I want to add products to my cart so I can purchase them later.

    Acceptance Criteria:
    - Clicking "Add to cart" button adds the item to the cart
    - Cart badge updates immediately with the correct count
    - Button changes to "Remove" after item is added
    - Clicking "Remove" removes the item and badge decrements
    - Cart persists if user navigates to another page and returns
    - Maximum 6 items can be added (one of each product)

    Tech Stack: React frontend, REST API, session-based cart storage
    """
    
    # Call the function and store the result
    prompt = generate_test_case_prompt(feature)
    
    # Print the prompt to the console
    print(prompt)