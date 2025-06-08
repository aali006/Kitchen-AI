# ---- run.py ----
from app.interface import create_interface

if __name__ == "__main__":
    iface = create_interface()
    iface.launch(server_name="0.0.0.0", server_port=7860, share=True)