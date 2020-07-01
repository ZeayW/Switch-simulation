from DMA import DMA
from time import time, sleep
from threading import Timer

def test_dma():
  dma = DMA()
  dma.add(0xf2c4310521d9, 1)
  sleep(1)
  dma.add(0x014a256df202, 2)
  sleep(1)
  dma.add(0x010101010101, 3)
  sleep(1)
  dma.add(0xa10123124101, 4)
  sleep(1)
  dma.add(0xff0000000000, 5)
  sleep(1)
  dma.query(0x010101010101)
  sleep(1)
  dma.query(0xaaaaaaaaaaaa)
  sleep(1)
  dma.query(0xf2c4310521d9)
  sleep(5)
  dma.__stop__()

if __name__ == "__main__":
  test_dma()
