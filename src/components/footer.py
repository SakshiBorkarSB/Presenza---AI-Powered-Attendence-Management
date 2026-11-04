
import streamlit as st

def footer_home():
    st.html("""
        <style>
            .classora-footer {
                position: fixed;
                bottom: 10px;
                right: 20px;
                z-index: 999999;
                text-align: right;
                pointer-events: none;
            }

            .classora-footer p {
                color: #D4C5F5;
                font-size: 14px;
                margin: 0;
                letter-spacing: 0.4px;
            }

            .classora-footer span {
                font-weight: 600;
            }
        </style>

        <div class="classora-footer">
            <p>
                © 2026 <span>Classora</span>
                · AI-Powered Attendance Management
            </p>
        </div>
    """)
