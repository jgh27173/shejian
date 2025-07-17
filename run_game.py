import http.server
import socketserver
import webbrowser
import os
import threading
import sys

# 配置项
PORT = 8000  # 服务器端口
AUTO_OPEN = True  # 是否自动打开浏览器

def start_server():
    """启动本地 HTTP 服务器"""
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    # 尝试多个端口，避免冲突
    for port in range(PORT, PORT + 10):
        try:
            Handler = http.server.SimpleHTTPRequestHandler
            with socketserver.TCPServer(("", port), Handler) as httpd:
                print(f"服务器已启动：http://localhost:{port}")
                print(f"游戏目录：{current_dir}")
                print("按 Ctrl+C 停止服务器")
                
                # 自动打开浏览器
                if AUTO_OPEN:
                    threading.Thread(target=open_browser, args=(port,)).start()
                
                httpd.serve_forever()
            break
        except OSError:
            print(f"端口 {port} 被占用，尝试 {port + 1}...")

def open_browser(port):
    """打开浏览器访问服务器"""
    import time
    time.sleep(1)  # 等待服务器启动
    url = f"http://localhost:{port}"
    
    # 优先使用 Chrome 或 Firefox（兼容性更好）
    browsers = [
        "chrome", "google-chrome", 
        "firefox", "mozilla-firefox"
    ]
    
    for browser in browsers:
        try:
            webbrowser.get(browser).open(url)
            print(f"已使用 {browser} 打开浏览器")
            return
        except:
            continue
    
    # 默认浏览器
    webbrowser.open(url)
    print("已使用默认浏览器打开")

if __name__ == "__main__":
    start_server()