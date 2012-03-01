;;; .emacs.el --- GNU Emacs �ѽ�����ե�����

;; ���ܸ�Ķ��Υ��åȥ��å�
(set-language-environment "Japanese")
(set-default-coding-systems 'utf-8)
(set-buffer-file-coding-system 'utf-8)
(set-terminal-coding-system 'utf-8)
(set-keyboard-coding-system 'utf-8)
(setq-default buffer-file-coding-system 'utf-8)
(prefer-coding-system 'utf-8)
(setq default-process-coding-system (cons 'utf-8 'utf-8))

;; ��.emacs.d�פΥե����뷲���ɤ�
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


;; ����Ū������
(setq user-mail-address
      "tanarky@gmail.com")      ; �᡼�륢�ɥ쥹
(setq inhibit-startup-message t)        ; Emacs ��ư��å���������ɽ��
(setq scroll-step 2)                    ; ���̥�������οʤ���
(setq column-number-mode t)             ; ������ɽ������
;; (setq-default transient-mark-mode t)    ; �ޡ�����ɽ��
(setq-default fill-column 74)           ; �ǥե���ȤΥƥ����ȥ���� (�ܰ�)
(setq search-highlight t)               ; �������˥ϥ��饤�Ȥ���
(setq query-replace-highlight t)        ; �ִ����˥ϥ��饤�Ȥ���
;(setq visible-bell t)                    �ӡ��פ� visible �ˤ���
(setq automatic-hscrolling t)           ; ��ʿ��������󥰤�ͭ��
(auto-compression-mode t)               ; ���̥ե������ư�ǰ���
(setq dired-recursive-deletes 'top)     ; Dired �ǺƵ�Ū�˥ǥ��쥯�ȥ���
(setq dired-recursive-copies t)         ; Dired �ǺƵ�Ū�˥ǥ��쥯�ȥ�ʣ��
(setq next-line-add-newlines nil)       ; �Хåե��κǸ�ǹԤ�������ʤ�
(setq quail-japanese-use-double-n t)    ; quail �� `nn' �ǡ֤�פ����Ϥ��롣
(setq custom-file                       ; ��������ե�����̾
      "~/.emacs.d/99custom.el")
(and (fboundp 'auto-image-file-mode)    ; �����ե������ư�ǰ���
     (auto-image-file-mode t))
(put 'narrow-to-region 'disabled nil)   ; narrow-to-region ��ͭ����

;; �ץ���ߥ󥰴ط�
(setq c-default-style "cc-mode")        ; C �Υǥե���ȥ�������
(setq comment-multi-line t)             ; C-j �ǥ����Ȥ�ʣ���Ԥˤޤ�������
(setq-default indent-tabs-mode nil)     ; ����ǥ�Ȥ˥���ʸ������Ѥ��ʤ�
(setq c-tab-always-indent nil)          ; TAB ��á���Ⱦ�˥���ǥ�Ȥ��뤫
;(c-set-offset 'case-label '+)          ; case ���ơ��ȥ��Ȥǥ���ǥ�Ȥ���
(setq scheme-program-name "gosh")

;; font-lock (ʸ������) �˴ؤ������
(global-font-lock-mode 1)               ; ��� font-lock ����
(setq font-lock-maximum-decoration t)   ; ���Ϥ� font-lock ����
(show-paren-mode t)                     ; �б����å���ɽ������
(setq show-paren-style "parenthesis")   ; �б����å�����餻��
(and (boundp 'show-trailing-whitespace) ; �����ζ����ɽ�����뤫
     (setq-default
      show-trailing-whitespace nil))

;; �ɲäΥ����ޥå�
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


