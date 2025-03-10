## user story for poll app

สมปองเปิด url สำหรับ poll app
สมปองเห็นคำถามหลายข้อ
สมปองคลิ๊กที่คำถามข้อแรก
ทำการ redirect ไปที่หน้า detail แสดง คำถาม ตัวเลือก A,B
สมปองเลือกตัวเลือก A และกด submit
สมปองถูกส่งไปที่หน้าแสดง result แสดงจำนวนครั้งที่เลือก A,B ก่อนหน้านี้รวมกับของตน
สมปองกด back เพื่อกลับสู่หน้าคำถาม




## venv มีปัญหาไม่สามารถรันได้

╰─❯ php manage.py runserver
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "superlists.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
