import streamlit as st


def debug_code(code):
    """Debugs Python code using Gemini API."""
    prompt = f"""
    Analyze the following Python code for errors and suggest fixes.
    Provide the corrected code along with explanations.

    ```python
    {code}
    ```

    Output the corrected code in a code block, and provide a short explanation of the changes.
    """

    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error debugging code: {e}"

# Streamlit App
def main():
    st.title("Automated Code Debugging Helper")

    code_input = st.text_area("Enter Python code to debug:")

    if st.button("Debug Code"):
        if code_input:
            with st.spinner("Debugging code..."):
                debug_result = debug_code(code_input)

            if debug_result:
                st.subheader("Debugging Result:")
                st.markdown(debug_result)

                # Show original and corrected code side-by-side (if possible)
                if "```python" in debug_result:
                    corrected_code = debug_result.split("```python")[1].split("```")[0].strip()
                    col1, col2 = st.columns(2)
                    with col1:
                        st.subheader("Original Code:")
                        st.code(code_input, language="python")
                    with col2:
                        st.subheader("Corrected Code:")
                        st.code(corrected_code, language="python")
                else:
                    st.write("Could not extract corrected code. Full response shown above.")

            else:
                st.error("Code debugging failed. Please try again.")
        else:
            st.warning("Please enter some Python code.")

if __name__ == "__main__":
    main()
