import os
from typing import Any, Optional
import argparse
from llama_index.llms.openai_like import OpenAILike

class Typhoon(OpenAILike):
    def __init__(
        self,
        model: str,
        api_key: Optional[str] = None,
        api_base: str = "https://api.opentyphoon.ai/v1",
        is_chat_model: bool = True,
        is_function_calling_model: bool = True,
        **kwargs: Any,
    ) -> None:
        api_key = api_key or os.environ.get("Typhoon_API_KEY", None)
        super().__init__(
            model=model,
            api_key=api_key,
            api_base=api_base,
            is_chat_model=is_chat_model,
            is_function_calling_model=is_function_calling_model,
            **kwargs,
        )

    @classmethod
    def class_name(cls) -> str:
        return "Typhoon"

def main():
    parser = argparse.ArgumentParser(description="Typhoon CLI")
    parser.add_argument("--model", required=True, help="Model name")
    parser.add_argument("--api_key", help="API key")
    args = parser.parse_args()

    typhoon_instance = Typhoon(model=args.model, api_key=args.api_key)
    print(f"Class Name: {typhoon_instance.class_name()}")

if __name__ == "__main__":
    main()
