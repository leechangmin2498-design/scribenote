"""
PDF 텍스트 추출 프로그램
repository/pdfs 폴더에 있는 모든 PDF 파일에서 텍스트를 추출합니다.
"""

import os
from pathlib import Path
from pypdf import PdfReader


def extract_text_from_pdf(pdf_path):
    """
    PDF 파일에서 텍스트를 추출합니다.
    
    Args:
        pdf_path: PDF 파일 경로
        
    Returns:
        추출된 텍스트 문자열
    """
    try:
        reader = PdfReader(pdf_path)
        text = ""
        
        print(f"처리 중: {os.path.basename(pdf_path)} ({len(reader.pages)} 페이지)")
        
        for page_num, page in enumerate(reader.pages, start=1):
            page_text = page.extract_text()
            text += f"\n--- 페이지 {page_num} ---\n"
            text += page_text
            text += "\n"
        
        return text
    except Exception as e:
        print(f"오류 발생 ({pdf_path}): {str(e)}")
        return None


def extract_all_pdfs(pdf_folder, output_folder=None):
    """
    폴더 내 모든 PDF 파일에서 텍스트를 추출합니다.
    
    Args:
        pdf_folder: PDF 파일들이 있는 폴더 경로
        output_folder: 추출된 텍스트를 저장할 폴더 (None이면 pdf_folder와 같은 위치에 저장)
    """
    pdf_folder = Path(pdf_folder)
    
    if not pdf_folder.exists():
        print(f"폴더를 찾을 수 없습니다: {pdf_folder}")
        return
    
    # 출력 폴더 설정
    if output_folder is None:
        output_folder = pdf_folder.parent / "extracted_texts"
    else:
        output_folder = Path(output_folder)
    
    output_folder.mkdir(exist_ok=True)
    
    # PDF 파일 찾기
    pdf_files = list(pdf_folder.glob("*.pdf"))
    
    if not pdf_files:
        print(f"PDF 파일을 찾을 수 없습니다: {pdf_folder}")
        return
    
    print(f"\n총 {len(pdf_files)}개의 PDF 파일을 찾았습니다.\n")
    
    # 각 PDF 파일 처리
    for pdf_file in pdf_files:
        print(f"\n{'='*60}")
        text = extract_text_from_pdf(pdf_file)
        
        if text:
            # 텍스트 파일로 저장
            output_file = output_folder / f"{pdf_file.stem}.txt"
            with open(output_file, "w", encoding="utf-8") as f:
                f.write(text)
            print(f"저장 완료: {output_file}")
        else:
            print(f"텍스트 추출 실패: {pdf_file.name}")
    
    print(f"\n{'='*60}")
    print(f"모든 작업이 완료되었습니다!")
    print(f"추출된 텍스트는 다음 폴더에 저장되었습니다: {output_folder}")


if __name__ == "__main__":
    # PDF 폴더 경로 설정
    script_dir = Path(__file__).parent
    pdf_folder = script_dir / "repository" / "pdfs"
    
    # 텍스트 추출 실행
    extract_all_pdfs(pdf_folder)
