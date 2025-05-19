import os
import json

def build_video_pairs(video_root='video', baselines=('asva', 'ours'), output_file='video_pairs.json'):
    baseline_a, baseline_b = baselines
    pairs = []

    # 기준: baseline_a에서 class_name 디렉터리와 파일 목록 확인
    for class_name in sorted(os.listdir(os.path.join(video_root, baseline_a))):
        class_dir_a = os.path.join(video_root, baseline_a, class_name)
        class_dir_b = os.path.join(video_root, baseline_b, class_name)

        if not os.path.isdir(class_dir_a) or not os.path.isdir(class_dir_b):
            continue

        for filename in sorted(os.listdir(class_dir_a)):
            if not filename.endswith(".mp4"):
                continue

            path_a = os.path.join(class_dir_a, filename)
            path_b = os.path.join(class_dir_b, filename)

            if os.path.exists(path_b):
                pairs.append({
                    baselines[0]: path_a.replace("\\", "/"),
                    baselines[1]: path_b.replace("\\", "/"),
                    "prompt": class_name.replace("_", " ")
                })

    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(pairs, f, indent=2, ensure_ascii=False)

    print(f"{len(pairs)} pairs saved to {output_file}")

# 실행 예시
if __name__ == "__main__":
    build_video_pairs()
