import subprocess
import os
import re

def get_git_status():
    """
    현재 Git 저장소에서 변경되거나 새로 생성된(Untracked) 파일 목록을 가져옵니다.
    """
    # 'git status --porcelain'은 스크립트에서 읽기 쉬운 형식으로 상태를 출력합니다.
    result = subprocess.run(['git', 'status', '--porcelain'], capture_output=True, text=True)
    lines = result.stdout.strip().split('\n')
    
    changed_files = []
    for line in lines:
        if not line:
            continue
        # 상태 코드(M, A, ?? 등) 뒤의 파일 경로만 추출
        file_path = line[3:].strip()
        # .py 파일이고 이름이 숫자로 시작하는 경우만 필터링 (예: 1234.py)
        if file_path.endswith('.py') and re.match(r'^\d+', os.path.basename(file_path)):
            changed_files.append(file_path)
            
    return changed_files

def git_commit_per_file(file_path):
    """
    파일별로 git add 및 문제 번호를 포함한 커밋을 수행합니다.
    """
    # 파일명에서 문제 번호 추출 (예: '1000.py' -> '1000')
    file_name = os.path.basename(file_path)
    problem_number = re.findall(r'\d+', file_name)[0]
    commit_message = f"https://www.acmicpc.net/problem/{problem_number}"

    try:
        # 1. git add {file_path}
        subprocess.run(['git', 'add', file_path], check=True)
        
        # 2. git commit -m "{commit_message}"
        subprocess.run(['git', 'commit', '-m', commit_message], check=True)
        
        print(f"✅ 성공: {file_name} -> Commit: {commit_message}")
    except subprocess.CalledProcessError as e:
        print(f"❌ 실패: {file_name} 에러 발생: {e}")

def main():
    changed_files = get_git_status()
    
    if not changed_files:
        print("점검할 변경된 파일이 없습니다.")
        return

    print(f"총 {len(changed_files)}개의 파일을 발견했습니다. 커밋을 시작합니다...\n")
    
    for file in changed_files:
        git_commit_per_file(file)
    
    # 선택 사항: 모든 커밋 후 한 번에 push 하려면 아래 주석을 해제하세요.
    # subprocess.run(['git', 'push'], check=True)
    # print("\n🚀 모든 변경 사항이 원격 저장소에 Push 되었습니다.")

if __name__ == "__main__":
    main()