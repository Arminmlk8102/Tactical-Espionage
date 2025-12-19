import pytest
import pygame
from final import reset_level, ScreenFade, BLACK, World,img_list
from unittest.mock import patch

pygame.init()  


def test_reset_level():
    data = reset_level()
    assert len(data) == 16
    for row in data:
        assert len(row) == 150
        assert all(tile == -1 for tile in row)

def test_screenfade_fade_counter_increments(monkeypatch):
    fade = ScreenFade(2, BLACK, 5)
    monkeypatch.setattr("pygame.draw.rect", lambda *a, **k: None)
    assert fade.fade_counter == 0
    fade_complete = fade.fade()
    assert fade.fade_counter == 5
    assert fade_complete == False

class DummySprite(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((10, 10))
        self.rect = self.image.get_rect()
        self.health = 100
        self.max_health = 100

def test_process_data_without_display():
    data = [[12, 11], [-1, -1]]  

    
    for i in range(len(img_list)):
        img_list[i] = pygame.Surface((10,10))

    
    with patch("final.Soldier", side_effect=lambda *a, **k: DummySprite()):
        with patch("final.HealthBar", side_effect=lambda *a, **k: DummySprite()):
            world = World()
            player, health_bar = world.process_data(data)

  
    assert world.level_length == len(data[0])
    
    assert player.health == 100
    assert health_bar.health == 100