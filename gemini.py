import streamlit as st
import google.generativeai as genai
import PyPDF2

# Gemini API 키 설정
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

# Gemini 모델 설정
model = genai.GenerativeModel('gemini-pro')

# PDF 파일 읽기 함수
def read_pdf(file_path):
    with open(file_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ""
        for page in reader.pages:
            text += page.extract_text()
    return text

# Streamlit 앱
def main():
    st.title('PDF 기반 Gemini AI 질문-답변 시스템')

    # PDF 파일 경로 (미리 지정된 파일)
    pdf_path = "attention.pdf"
    
    # PDF 내용 읽기
    pdf_text = read_pdf(pdf_path)

    # 사용자 입력
    user_input = st.text_input('질문을 입력하세요:')

    if user_input:
        # Gemini API로 응답 생성
        prompt = f"다음 내용을 바탕으로 질문에 답해주세요. 내용: {pdf_text}\n\n질문: {user_input}"
        response = model.generate_content(prompt)
        
        # 응답 표시
        st.write('AI 응답:')
        st.write(response.text)

if __name__ == "__main__":
    main()
