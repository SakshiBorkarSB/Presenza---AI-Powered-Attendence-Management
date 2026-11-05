
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
                color: #D4C5F5;
                font-size: 14px;
                font-weight: 500;
                margin: 0;
                letter-spacing: 0.4px;
            }

            .classora-footer span {
                font-weight: 600;
            }
        </style>

        <div class="classora-footer">
                © 2026 <span>Classora</span>
                · AI-Powered Attendance Management
        </div>
    """)

def footer_dashboard():
    st.html("""
        <style>
            .classora-footer {
                position: fixed;
                bottom: 10px;
                right: 20px;
                z-index: 999999;
                text-align: right;
                pointer-events: none;
                color: #35245F;
                font-size: 14px;
                font-weight: 500;
                margin: 0;
                letter-spacing: 0.4px;
            }

            .classora-footer span {
                font-weight: 600;
            }
        </style>

        <div class="classora-footer">
                © 2026 <span>Classora</span>
                · AI-Powered Attendance Management
        </div>
    """)