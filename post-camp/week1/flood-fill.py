class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        visited = [[0 for _ in range(len(image[0]))] for i in range(len(image))]
        def flood(pixel_row, pixel_col, color):
            if not (visited[pixel_row][pixel_col]):
                visited[pixel_row][pixel_col] = 1
                original_color = image[pixel_row][pixel_col]
                image[pixel_row][pixel_col] = color
                valid_pixels = []
                if (pixel_row > 0) and (image[pixel_row-1][pixel_col] == original_color):
                    valid_pixels.append([pixel_row-1, pixel_col])
    
                if (pixel_row < len(image)-1) and (image[pixel_row+1][pixel_col] == original_color):
                    valid_pixels.append([pixel_row+1, pixel_col])
    
                if (pixel_col > 0) and (image[pixel_row][pixel_col-1] == original_color):
                    valid_pixels.append([pixel_row, pixel_col-1])
    
                if (pixel_col < len(image[0])-1 and image[pixel_row][pixel_col+1] == original_color):
                    valid_pixels.append([pixel_row, pixel_col+1])
                
                for pixel in valid_pixels:
                    pixel_data = image[pixel[0]][pixel[1]]
                    if (pixel_data == original_color):
                        flood(pixel[0], pixel[1], color)
        
        flood(sr,sc, color)
        return image






