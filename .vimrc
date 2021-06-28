syntax on
filetype plugin indent on
let g:ctrlp_map = '<c-p>'
let g:ctrlp_cmd = 'CtrlP'

" set line numbers
set number

" map Tab and Shift+Tab to next and previous buffer
:nnoremap <Tab> :bnext<CR>
:nnoremap <S-Tab> :bprevious<CR>

" configure backspace behavior (fix for windows and macos)
set backspace=indent,eol,start

" enable ruler
set ruler

" move swap files to /tmp
set directory^=/tmp//

set encoding=utf-8

" always show the statusbar
set laststatus=2
