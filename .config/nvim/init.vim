" NEOVIM CONFIGURATION FILE                          


" Plugins
call plug#begin()
Plug 'junegunn/goyo.vim'
Plug 'junegunn/limelight.vim'
Plug 'itchyny/lightline.vim'
Plug 'dracula/vim'
Plug 'easymotion/vim-easymotion'
Plug 'lambdalisue/suda.vim'
" Search
Plug 'jremmen/vim-ripgrep'
call plug#end()

" Changing <leader> key
let mapleader = " "

" Copy and paste to/from clipboard
set clipboard+=unnamedplus

" Press 'W' to write file with sudo privileges
com W :execute 'SudaWrite'

" Easymotion configuration
let g:EasyMotion_off_screen_search = 0
map <leader>f <Plug>(easymotion-bd-w)
map <leader>а <Plug>(easymotion-bd-w)

" Define lightline configuration
let g:lightline = {
      \ 'colorscheme': 'dracula',
      \ 'active': { 
      \   'right': [ [ 'lineinfo' ],
      \              [ 'percent' ] ] },	
      \ }

set noshowmode " remove '--insert--' from below the statusline

" Configuring Goyo and Limelight plugins
autocmd! User GoyoEnter Limelight
autocmd! User GoyoLeave Limelight!

" map <A-l> :Limelight!!0.8 <CR>
" map <A-g> :Goyo <CR>
nnoremap <leader>g :Goyo <CR>
nnoremap <leader>п :Goyo <CR>

let g:limelight_conceal_ctermfg = 'gray'
let g:limelight_conceal_ctermfg = 240

" Search in a directory
nnoremap <leader>t :Rg 

" Clear search highlighting
nnoremap <CR> :noh<CR>

" Case insensitive search
:set ic

" Working with multiple windows
nnoremap <Leader>w <C-w>w
nnoremap <Leader>q <C-w>q

" Getting russian keyboard layout to work
:set langmap=ФИСВУАПРШОЛДЬТЩЗЙКЫЕГМЦЧНЯ;ABCDEFGHIJKLMNOPQRSTUVWXYZ,фисвуапршолдьтщзйкыегмцчня;abcdefghijklmnopqrstuvwxyz

" Fixing alacritty bug
" autocmd VimEnter * :sleep 20m
autocmd VimEnter * :silent exec "!kill -s SIGWINCH $PPID"
