import streamlit as st

def subject_card(name, code, section, stats=None, footer_callback=None, min_height=None):

    height_style = f"min-height: {min_height}px;" if min_height else ""

    html = f"""
        <div style="
            background: #F5F0FF;
            border-left: 1.5px solid #523B91;
            padding: 20px;
            padding-top: 20px;
            border-radius: 12px;
            border: 1.5px solid #523B91;
            margin-bottom: 20px;
            {height_style}
        ">
            <h4 style="margin: 0; color: #35245F; padding: 0;">{name}</h4>
            <p style="color: #35245F; margin: 10px 0;">
                Code: <span style="background: #E6D9FF; color: #35245F; padding: 2px 8px; border-radius: 5px;">{code}</span>
                | Section: {section}
            </p>
        """

    if stats:
        html += """
        <div style="display: flex; gap: 8px; flex-wrap: wrap; color: #35245F;">
        """

        for icon, label, value in stats:
            html += f'<div style="background: #E6D9FF; padding: 5px 12px; border-radius: 8px; font-size: 0.9rem">{icon} <b>{value}</b> {label}</div>'

        html += "</div>"

    html += "</div>"

    st.markdown(html, unsafe_allow_html=True)

    if footer_callback:
        footer_callback()