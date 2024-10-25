파이썬 라이브러리를 GitHub에 두고 불러와 사용하는 방법은 크게 두 가지가 있습니다. 첫 번째는 Git 저장소를 패키지처럼 설치하는 것이고, 두 번째는 해당 저장소의 코드를 직접 불러와 사용하는 것입니다. 아래에 각 방법에 대해 설명해 드리겠습니다.

### 1. GitHub 저장소를 pip로 설치해서 사용하기

GitHub에 있는 라이브러리를 직접 설치하려면 `pip` 명령어를 사용하여 Git 저장소에서 설치할 수 있습니다. 다음과 같은 형식으로 GitHub URL을 이용해 패키지를 설치할 수 있습니다.

```bash
pip install git+https://github.com/username/repository.git
```

- `username`: GitHub 계정 이름입니다.
- `repository`: 설치하고자 하는 라이브러리가 있는 GitHub 저장소 이름입니다.

특정 브랜치나 커밋을 지정해서 설치하고 싶다면, 아래와 같이 옵션을 추가할 수 있습니다:

```bash
pip install git+https://github.com/username/repository.git@branch_or_commit
```

예시:
```bash
pip install git+https://github.com/username/my-python-lib.git@main
```

### 2. GitHub 저장소의 코드 불러와서 사용하기

또 다른 방법은 Git 저장소를 직접 로컬에 클론하고, 이를 파이썬에서 불러와 사용하는 것입니다.

#### 2.1 저장소 클론하기

먼저 터미널을 통해 원하는 디렉토리에 Git 저장소를 클론합니다.

```bash
git clone https://github.com/username/repository.git
```

#### 2.2 클론한 저장소 경로를 PYTHONPATH에 추가

클론한 코드가 있는 디렉토리를 파이썬의 모듈 경로에 추가하여 코드를 바로 사용할 수 있게 설정합니다. 예를 들어, `my-python-lib`라는 폴더에 클론했다면 아래와 같이 할 수 있습니다.

```python
import sys
sys.path.append('/path/to/your/cloned/repository')
```

그 후에 해당 모듈을 일반적인 파이썬 모듈처럼 불러올 수 있습니다.

```python
import my_python_lib
```

### 3. `setup.py`를 이용한 설치

GitHub에 있는 라이브러리가 `setup.py` 파일을 포함하고 있다면, 클론 후 설치할 수도 있습니다.

```bash
git clone https://github.com/username/repository.git
cd repository
pip install .
```

이렇게 하면 시스템에 해당 패키지가 설치되며, 일반적인 라이브러리처럼 어디서든 불러올 수 있게 됩니다.

### 4. `requirements.txt` 파일에 GitHub 링크 사용하기

만약 프로젝트에서 GitHub에 있는 라이브러리를 종속성으로 추가하고 싶다면, `requirements.txt` 파일에 아래와 같이 Git URL을 추가할 수 있습니다:

```text
git+https://github.com/username/repository.git
```

그 후에, `pip`로 설치할 수 있습니다:

```bash
pip install -r requirements.txt
```

이렇게 하면 프로젝트를 구성할 때 GitHub 라이브러리도 함께 설치됩니다.

### 요약

- **pip 명령어로 GitHub 저장소에서 설치**: `pip install git+https://github.com/username/repository.git`
- **Git 저장소를 로컬에 클론한 후 경로 추가**: `sys.path.append('/path/to/your/cloned/repository')`
- **requirements.txt에 GitHub URL 추가**: `requirements.txt` 파일에 Git URL 추가 후 설치

이런 방법들을 통해 GitHub에 있는 파이썬 라이브러리를 손쉽게 불러와 사용할 수 있습니다.