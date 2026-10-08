# Git 常用命令速查

## 一、首次配置（每台机器只做一次）

```bash
git config --global user.name "en0505"
git config --global user.email "1271376833@qq.com"
git config --global --list          # 复核
```

## 二、日常四步曲

```bash
git status                  # 看现在什么情况（最常用，拿不准就敲它）
git add .                   # 把改动放进暂存区
git commit -m "说明这次改了什么"
git push                    # 推到 GitHub
```

## 三、看清自己改了什么

```bash
git diff                    # 还没暂存的改动
git diff --staged           # 已经暂存、等着提交的改动
git log --oneline           # 简洁的提交历史
git log --oneline --graph --all   # 带分支线的历史图
git show HEAD               # 看最近一次提交的详细内容
```

## 四、撤销与回退

```bash
git restore 文件名              # 丢弃未提交的改动（危险，不可恢复）
git restore --staged 文件名     # 把文件移出暂存区，改动保留
git switch 分支名               # 切换分支
git switch -c 新分支名          # 新建并切过去
```

## 五、分支与合并

```bash
git branch                  # 列出分支，* 是当前所在
git merge 分支名            # 把某分支合并进当前分支
git branch -d 分支名        # 删除已合并的分支
```

## 六、与 GitHub 交互

```bash
git clone <仓库地址>                    # 把别人的仓库整个拉下来
git remote add origin <仓库地址>        # 关联远程仓库
git remote -v                          # 查看已关联的远程
git push -u origin main                # 首次推送，-u 记住上游
git pull                               # 把远程的新提交拉下来
```

## 七、几条实战经验

1. **拿不准就先 `git status`**，它会告诉你下一步该干什么。
2. **提交信息写清楚**。"修复 bug" 是坏习惯，"修复登录页验证码不刷新" 才是好习惯。
3. **密钥、密码、本地配置永远不要提交**，写进 `.gitignore`。
4. **一个提交只做一件事**，改动太大就拆成几次提交。
5. `push` 之前先 `pull`，能少碰很多冲突。
