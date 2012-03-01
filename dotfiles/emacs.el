;;; .emacs.el --- GNU Emacs 用初期化ファイル

;; 日本語環境のセットアップ
(set-language-environment "Japanese")
(set-default-coding-systems 'utf-8)
(set-buffer-file-coding-system 'utf-8)
(set-terminal-coding-system 'utf-8)
(set-keyboard-coding-system 'utf-8)
(setq-default buffer-file-coding-system 'utf-8)
(prefer-coding-system 'utf-8)
(setq default-process-coding-system (cons 'utf-8 'utf-8))

;; 「.emacs.d」のファイル群を読む
(save-match-data
  (and (file-directory-p "~/.emacs.d")
       (let ((files (sort (directory-files "~/.emacs.d") #'string<))
             file)
         (while (setq file (car files))
           (setq file (concat "~/.emacs.d/" file))
           (if (and (file-readable-p file)
                    (string-match "\.el$" file)
                    (not (file-directory-p file))
                    (not (backup-file-name-p file)))
               (load-file file))
           (setq files (cdr files))))))


;; 一般的な設定
(setq user-mail-address
      "tanarky@gmail.com")      ; メールアドレス
(setq inhibit-startup-message t)        ; Emacs 起動メッセージを非表示
(setq scroll-step 2)                    ; 画面スクロールの進み幅
(setq column-number-mode t)             ; カラムを表示する
;; (setq-default transient-mark-mode t)    ; マークの表示
(setq-default fill-column 74)           ; デフォルトのテキストカラム (目安)
(setq search-highlight t)               ; 検索時にハイライトする
(setq query-replace-highlight t)        ; 置換時にハイライトする
;(setq visible-bell t)                    ビープを visible にする
(setq automatic-hscrolling t)           ; 水平スクローリングを有効
(auto-compression-mode t)               ; 圧縮ファイルを自動で扱う
(setq dired-recursive-deletes 'top)     ; Dired で再帰的にディレクトリ削除
(setq dired-recursive-copies t)         ; Dired で再帰的にディレクトリ複製
(setq next-line-add-newlines nil)       ; バッファの最後で行を作成しない
(setq quail-japanese-use-double-n t)    ; quail で `nn' で「ん」を入力する。
(setq custom-file                       ; カスタムファイル名
      "~/.emacs.d/99custom.el")
(and (fboundp 'auto-image-file-mode)    ; 画像ファイルを自動で扱う
     (auto-image-file-mode t))
(put 'narrow-to-region 'disabled nil)   ; narrow-to-region を有効に

;; プログラミング関係
(setq c-default-style "cc-mode")        ; C のデフォルトスタイル
(setq comment-multi-line t)             ; C-j でコメントを複数行にまたがせる
(setq-default indent-tabs-mode nil)     ; インデントにタブ文字を使用しない
(setq c-tab-always-indent nil)          ; TAB を叩くと常にインデントするか
;(c-set-offset 'case-label '+)          ; case ステートメントでインデントする
(setq scheme-program-name "gosh")

;; font-lock (文字装飾) に関する指定
(global-font-lock-mode 1)               ; 常に font-lock する
(setq font-lock-maximum-decoration t)   ; 全力で font-lock する
(show-paren-mode t)                     ; 対応カッコを表示する
(setq show-paren-style "parenthesis")   ; 対応カッコを光らせる
(and (boundp 'show-trailing-whitespace) ; 行末の空白を表示するか
     (setq-default
      show-trailing-whitespace nil))

;; 追加のキーマップ
(global-set-key (kbd "ESC M-%") 'query-replace-regexp)
(global-set-key (kbd "ESC M-:") 'eval-region)
(global-set-key (kbd "ESC M-<") 'beginning-of-buffer-other-window)
(global-set-key (kbd "C-x 4 s") 'reishi-open-term-other-window)
(global-set-key (kbd "C-x C-p") 'reishi-other-window-backward)
(global-set-key (kbd "C-x C-n") 'other-window)
(global-set-key (kbd "C-x C-q") 'view-mode)
(global-set-key (kbd "C-x l")   'goto-line)
(global-set-key (kbd "M-p")     'backward-paragraph)
(global-set-key (kbd "M-n")     'forward-paragraph)
(global-set-key (kbd "C-h")     'backward-delete-char)
(global-set-key [C-tab]         'bury-buffer)
(global-set-key [delete]        'backward-delete-char)
(global-set-key [home]          'beginning-of-buffer)
(global-set-key [end]           'end-of-buffer)

;(display-time)
;(display-battery)

;;load-library "php-mode")
;;(require 'php-mode)
(autoload 'php-mode "php-mode" "Major mode for editing php code." t)

;; ruby-mode
;;(autoload 'ruby-mode "ruby-mode"
;;  "Mode for editing ruby source files" t)
;;(setq auto-mode-alist
;;      (append '(("\\.rb$" . ruby-mode)) auto-mode-alist))
;;(setq interpreter-mode-alist (append '(("ruby" . ruby-mode))
;;                                     interpreter-mode-alist))
;;(autoload 'run-ruby "inf-ruby"
;;  "Run an inferior Ruby process")
;;(autoload 'inf-ruby-keys "inf-ruby"
;;  "Set local key defs for inf-ruby in ruby-mode")
;;(add-hook 'ruby-mode-hook
;;          '(lambda ()
;;             (inf-ruby-keys)))

;; haskell-mode
;;(load-library "haskell-mode")
;;(require 'haskell-mode)
;;(setq auto-mode-alist
;;      (append '(("\\.hs$" . haskell-mode)) auto-mode-alist))

;;;; javascript-mode
;;(add-to-list 'auto-mode-alist (cons  "\\.\\(js\\|as\\|json\\|jsn\\)\\'" 'javascript-mode))
;;(autoload 'javascript-mode "javascript" nil t)
;;(setq js-indent-level 4)

;; js2-mode
(autoload 'js2-mode "js2" nil t)
(add-to-list 'auto-mode-alist '("\\.js$" . js2-mode))

;; css-mode
;;(load-library "css-mode")
;;(require 'css-mode)
;;(add-to-list 'auto-mode-alist (cons  "\\.css\\'" 'css-mode))
;;(autoload 'css-mode "css" nil t)

(menu-bar-mode -1)
;;; .emacs.el ends here


