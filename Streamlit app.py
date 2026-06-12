import streamlit as st
from google import genai
import os

# تصميم واجهة الموقع
st.set_page_config(page_title="Solar Nile2Sky AI", page_icon="🌱", layout="centered")

st.title("🌱 محطة طاقة ورد النيل الذكية")
st.subheader("مشروع الطالبة: حبيبة أشرف - سوهاج")
st.write("هذا النظام يدار بالكامل بواسطة الذكاء الاصطناعي Gemini لإدارة وتدوير ورد النيل.")

# إدخال الـ API Key
api_key = st.text_input("أدخل مفتاح Gemini API الخاص بك:", type="password")

if api_key:
    # ربط النظام بجوجل
    client = genai.Client(api_key=api_key)
    
    # القائمة الجانبية للتنقل بين وظائف الـ AI
    option = st.sidebar.selectbox(
        "اختر مهمة الذكاء الاصطناعي:",
        ["1. التنبؤ بإنتاج الطاقة والسماد", "2. شات بوت خدمة المزارعين"]
    )
    
    # ---- المهمة الأولى: التنبؤ بالطاقة ----
    if option == "1. التنبؤ بإنتاج الطاقة والسماد":
        st.header("📊 نظام التنبؤ الرقمي بالإنتاج")
        weight = st.number_input("أدخل وزن ورد النيل المحصود (بالكيلوجرام):", min_value=10, value=100)
        
        if st.button("احسب العائد المتوقع"):
            with st.spinner("جاري حساب البيانات عبر Gemini..."):
                prompt = f"بناءً على أبحاث الكربنة الحرارية المائية، إذا طبخنا {weight} كيلو ورد نيل، احسب بالملي باختصار: كمية وقود الطائرات SAF، كمية المياه المقطرة، وكمية الفحم الحيوي الناتجة؟"
                response = client.models.generate_content(model='gemini-2.5-flash', contents=prompt)
                st.success("✨ النتائج المتوقعة من الطبخة الكيميائية:")
                st.write(response.text)
                
    # ---- المهمة الثانية: شات بوت المزارعين ----
    elif option == "2. شات بوت خدمة المزارعين":
        st.header("💬 مساعد مزارعي سوهاج الذكي")
        st.write("الـ AI هنا بيقنع المزارعين في الصعيد يشتروا السماد العضوي لزيادة محاصيلهم.")
        
        user_msg = st.text_input("اكتب رسالتك للـ AI (مثال: السماد ده بيعمل إيه وأقرب فرع فين؟)")
        
        if st.button("إرسال"):
            with st.spinner("جاري رد المهندس الذكي..."):
                system_instruction = "أنت ممثل خدمة عملاء ذكي لمحطة طاقة نيل تو سكاي في سوهاج. نبيع سماد عضوي من ورد النيل يرفع الإنتاجية 30%. تحدث بلهجة صعيدية ودودة جداً واقنع العميل."
                response = client.models.generate_content(
                    model='gemini-2.5-flash',
                    contents=user_msg,
                    config={"system_instruction": system_instruction}
                )
                st.chat_message("assistant").write(response.text)
else:
    st.info("🔑 يرجى إدخال الـ API Key في الأعلى لتفعيل العقل الذكي للموقع.")
