# ScribeNote - PDF 텍스트 추출 도구

`repository/pdfs` 폴더에 있는 모든 PDF 파일에서 텍스트를 자동으로 추출하는 Python 프로그램입니다.

**작성자**: 이창민  
**리뷰어**: 정화수, 김명훈, 김현철

## 📋 프로젝트 개요

이 프로젝트는 학술 논문 PDF 파일들의 텍스트를 일괄 추출하여 텍스트 파일로 저장하는 도구입니다. 현재 5개의 논문 PDF 파일을 처리할 수 있습니다.

## ✨ 주요 기능

- **자동 일괄 처리**: 폴더 내 모든 PDF 파일을 자동으로 찾아 처리
- **페이지별 구조화**: 각 페이지를 구분하여 텍스트 추출
- **자동 폴더 생성**: 출력 폴더가 없으면 자동으로 생성
- **진행 상황 표시**: 실시간으로 처리 진행 상황 출력
- **오류 처리**: 파일 읽기 오류 및 예외 상황 안전하게 처리

## 📁 프로젝트 구조

```
scribenote/
├── extract_pdf_text.py      # 메인 프로그램
├── requirements.txt          # 패키지 의존성
├── README.md                 # 프로젝트 설명서
├── Report/                   # 작업 리포트
│   └── 작업_리포트.md
└── repository/
    ├── pdfs/                 # 입력 PDF 파일들
    └── extracted_texts/      # 출력 텍스트 파일들 (자동 생성)
```

## 🚀 빠른 시작

### 1. 필수 요구사항

- Python 3.7 이상
- pip 패키지 관리자

### 2. 설치

```bash
# 필요한 패키지 설치
pip install -r requirements.txt
```

### 3. 실행

```bash
python extract_pdf_text.py
```

## 📖 사용 방법

1. **PDF 파일 준비**: `repository/pdfs/` 폴더에 PDF 파일을 넣습니다.

2. **프로그램 실행**: 
   ```bash
   python extract_pdf_text.py
   ```

3. **결과 확인**: 추출된 텍스트는 `repository/extracted_texts/` 폴더에 저장됩니다.

## 📤 출력 형식

- 각 PDF 파일마다 하나의 `.txt` 파일이 생성됩니다.
- 파일명은 원본 PDF 파일명과 동일하며, 확장자만 `.txt`로 변경됩니다.
- 각 텍스트 파일은 페이지 번호와 함께 구조화되어 저장됩니다.

**예시:**
```
--- 페이지 1 ---
[페이지 1의 텍스트 내용]

--- 페이지 2 ---
[페이지 2의 텍스트 내용]
...
```

## 📚 처리 대상 파일

현재 `repository/pdfs` 폴더에 있는 PDF 파일:

1. Attention Is All You Need-1706.03762v7.pdf
2. Efficient Estimation of Word Representations in-1301.3781v3.pdf
3. Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks-2005.11401v4.pdf
4. Training language models to follow instructions-2203.02155v1.pdf
5. Universal Language Model Fine-tuning for Text Classification-1801.06146v5.pdf

## 🛠️ 기술 스택

- **Python 3.x**: 프로그래밍 언어
- **pypdf**: PDF 파일 읽기 및 텍스트 추출 라이브러리
- **pathlib**: 경로 처리 및 파일 시스템 작업

## 📝 주요 함수

### `extract_text_from_pdf(pdf_path)`
단일 PDF 파일에서 텍스트를 추출합니다.
- 입력: PDF 파일 경로
- 출력: 추출된 텍스트 문자열 (페이지별 구분)

### `extract_all_pdfs(pdf_folder, output_folder=None)`
폴더 내 모든 PDF 파일을 일괄 처리합니다.
- 입력: PDF 파일들이 있는 폴더 경로
- 출력: 각 PDF의 텍스트를 개별 `.txt` 파일로 저장

## ⚙️ 설정

기본 설정:
- 입력 폴더: `repository/pdfs/`
- 출력 폴더: `repository/extracted_texts/` (자동 생성)

출력 폴더를 변경하려면 `extract_pdf_text.py`의 `extract_all_pdfs()` 함수 호출 부분을 수정하세요.

## 🔍 예제 출력

프로그램 실행 시 다음과 같은 출력을 확인할 수 있습니다:

```
총 5개의 PDF 파일을 찾았습니다.

============================================================
처리 중: Attention Is All You Need-1706.03762v7.pdf (15 페이지)
저장 완료: repository/extracted_texts/Attention Is All You Need-1706.03762v7.txt
...
============================================================
모든 작업이 완료되었습니다!
추출된 텍스트는 다음 폴더에 저장되었습니다: repository/extracted_texts
```

## 📄 라이선스

이 프로젝트는 개인 사용 목적으로 개발되었습니다.

## 📞 문의

문제가 발생하거나 개선 사항이 있으면 이슈를 등록해주세요.

---

**개발일**: 2024년  
**프로젝트**: ScribeNote - PDF 텍스트 추출 도구
