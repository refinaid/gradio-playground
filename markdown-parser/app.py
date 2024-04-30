import gradio as gr

def get_text() -> str:
    return """\
# Hello Refinaid Markdown Parser

This is a markdown parser that will help you to summerize your ticket content.

- Author: [Hugo ChunHo Lin](https://github.com/1chooo)
- Date: 2024-04-30
- Version: v0.0.1

## Code Snippet

```python
def hello():
    print("Hello, Refinaid!")

if __name__ == "__main__":
    hello()
```

## Math Formula

$$ f(x) = x^2 + 2x + 1 $$

## Table
| Name | Age |
|------|-----|
| Hugo | 22  |

## Image
![Refinaid](https://avatars.githubusercontent.com/u/148614740?s=200&v=4)

## List
- Item 1
- Item 2

## Quote

> "The only way to do great work is to love what you do." - Steve Jobs

## Task List

- [x] Task 1
- [ ] Task 2

## Reference

- [refinaid/gradio-playground/markdown-parser](https://github.com/refinaid/gradio-playground)
"""

def render_preview(summerized_ticket_conent: str) -> str:
    return summerized_ticket_conent

with gr.Blocks(
    title='Refinaid Markdown Parser',
) as demo:
    
    gr.HTML(
        "<h1 align=center>Refinaid Markdown Parser</h1>"
    )
    
    with gr.Row():
        summerized_ticket_conent = gr.Textbox(
            interactive=True,
            label="📝 Summerized Ticket Content",
            render=True,
            value=get_text(),
        )
        prev_summerized_ticket_content = gr.Markdown(
            value=get_text(),
        )

    summerized_ticket_conent.change(
        fn=render_preview,
        inputs=summerized_ticket_conent,
        outputs=prev_summerized_ticket_content,
    )


demo.launch()

