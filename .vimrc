syntax on
filetype plugin indent on
let g:ctrlp_map = '<c-p>'
let g:ctrlp_cmd = 'CtrlP'

" simple auto indentation support
set smartindent

" set line numbers
set number

" toggle NERDTree with ctrl+n
map <silent> <C-n> :NERDTreeToggle<CR>

" map Tab and Shift+Tab to next and previous buffer
:nnoremap <Tab> :bnext<CR>
:nnoremap <S-Tab> :bprevious<CR>
