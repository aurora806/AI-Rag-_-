import os
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle


def create_pdf_reportlab(txt_filename, pdf_filename):
    # 1. 注册本地黑体字体
    font_path = "simhei.ttf"
    if not os.path.exists(font_path):
        print(f"找不到字体文件：{font_path}。请确保文件在当前目录下。")
        return

    # 注册字体，命名为 'SimHei'
    pdfmetrics.registerFont(TTFont('SimHei', font_path))

    # 2. 设置排版样式
    styles = getSampleStyleSheet()

    # 正文样式（关键：开启 wordWrap='CJK' 解决中文自动换行问题）
    body_style = ParagraphStyle(
        name='Body',
        fontName='SimHei',
        fontSize=11,
        leading=18,  # 行间距
        wordWrap='CJK'  # 强制中日韩字符按字换行
    )

    # 章节标题样式
    title_style = ParagraphStyle(
        name='Title',
        fontName='SimHei',
        fontSize=14,
        leading=22,
        spaceBefore=10,  # 段前间距
        spaceAfter=10  # 段后间距
    )

    # 3. 读取内容并逐行构建 PDF
    story = []
    try:
        with open(txt_filename, "r", encoding="utf-8") as f:
            for line in f:
                clean_line = line.strip()

                # 如果是空行，插入一段空白
                if not clean_line:
                    story.append(Spacer(1, 10))
                    continue

                # 识别章节标题
                if clean_line.startswith(("一、", "二、", "三、", "四、", "五、", "六、", "七、", "八、", "九、", "十、")):
                    story.append(Paragraph(clean_line, title_style))
                else:
                    # 正文内容
                    story.append(Paragraph(clean_line, body_style))

        # 4. 生成并保存 PDF
        doc = SimpleDocTemplate(pdf_filename, pagesize=A4)
        doc.build(story)
        print(f"🎉 成功！PDF 文件已生成：{pdf_filename}")

    except FileNotFoundError:
        print(f"错误：找不到 TXT 文件 '{txt_filename}'。")
    except Exception as e:
        print(f"发生未知错误：{e}")


if __name__ == "__main__":
    # 使用你截图中的实际文件名
    input_txt = "扫地机器人100问.txt"
    output_pdf = "扫地机器人100问.pdf"

    create_pdf_reportlab(input_txt, output_pdf)