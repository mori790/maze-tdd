import pygame
from .core import Maze
from .gen import RecursiveBacktracker
from .solve import BFSSolver

def run(width=20, height=12, seed=0, cell=32, margin=20, show_path=True):
    pygame.init()
    w = margin*2 + width*cell
    h = margin*2 + height*cell
    screen = pygame.display.set_mode((w,h))
    pygame.display.set_caption("Maze Viewer")
    
    def regen(s):
        m = Maze(width, height)
        RecursiveBacktracker(seed=s).generate(m)
        p = BFSSolver().solve(m, (0,0), (width-1, height-1)) if show_path else []
        return m, p
    maze, path = regen(seed)
    clock = pygame.time.Clock()
    running = True
    
    while running:
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                running = False
            elif ev.type == pygame.KEYDOWN:
                if ev.key == pygame.K_ESCAPE:
                    running = False
                elif ev.key == pygame.K_r:
                    maze, path = regen(seed)
                elif ev.key in (pygame.K_PLUS, pygame.K_EQUALS):
                    seed += 1; maze, path = regen(seed)
                elif ev.key == pygame.K_MINUS:
                    seed -= 1; maze, path = regen(seed)
                elif ev.key == pygame.K_p:
                    show_path = not show_path
                    if show_path:
                        _, path = regen(seed)
                    else:
                        path = []
        
        screen.fill((255, 255, 255))
        
        # 壁の描画
        black = (0,0,0)
        for y in range(height):
            for x in range(width):
                cx = margin + x * cell
                cy = margin + y * cell
                c = maze.cell(x, y)
                if "N" in c.walls:
                    pygame.draw.line(screen, black, (cx, cy), (cx+cell, cy), 2)
                if "S" in c.walls:
                    pygame.draw.line(screen, black, (cx, cy+cell), (cx+cell, cy+cell), 2)
                if "W" in c.walls:
                    pygame.draw.line(screen, black, (cx, cy), (cx, cy+cell), 2)
                if "E" in c.walls:
                    pygame.draw.line(screen, black, (cx+cell, cy), (cx+cell, cy+cell), 2)
        
        # 経路の描画
        if show_path and path:
            pts = []
            for (px, py) in path:
                vx = margin + px*cell + cell/2
                vy = margin + py*cell + cell/2
                pts.append((vx, vy))
            if len(pts) >= 2:
                pygame.draw.lines(screen, (200, 0, 0), False, pts, 4)
            pygame.draw.circle(screen, (0, 200, 0), pts[0], max(3, cell//6))  # start
            pygame.draw.circle(screen, (200, 0, 0), pts[-1], max(3, cell//6)) #goal
        
        font = pygame.font.SysFont(None, 20)
        info = f"W{width}xH{height} seed={seed} [R]egen [+/-]seed [P]ath [Esc]quit"
        screen.blit(font.render(info, True, (50, 50, 50)), (10, 5))
        
        pygame.display.flip()
        clock.tick(60)
    
    pygame.quit()

if __name__ == '__main__':
    run()