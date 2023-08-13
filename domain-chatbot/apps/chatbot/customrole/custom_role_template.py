
from .custom_role_model import CustomRoleModel


PROMPT = """
<s>[INST] <<SYS>>
{persona}
{scenario}
This is how {role_name} should talk
{examples_of_dialogue}
Then the roleplay chat between {you_name} and {role_name} begins.
This is the {you_name} and {role_name} memory module.
{long_history}
[{personality} {role_name} talks a lot with descriptions You only need to output {role_name}'s dialogue, no need to output {you_name}'s dialogue]
{short_history}
<</SYS>>
{you_name}：{input} [/INST]
"""

PERSONALITY_PROMPT = "{role_name}'s personality: {personality}"

SCENARIO_PROMPT = "Circumstances and context of the dialogue: {scenario}"


class CustomRoleTemplate():

    def format(self, custom_role_model: CustomRoleModel) -> str:

        # 获取prompt参数
        role_name = custom_role_model.role_name
        persona = custom_role_model.persona
        examples_of_dialogue = custom_role_model.examples_of_dialogue
        you_name = "{you_name}"
        long_history = "{long_history}"
        short_history = "{short_history}"
        input = "{input}"

        # 如果没有来自角色的第一段对话则填充为空
        first_message = custom_role_model.first_message
        if first_message == None:
            first_message = ''

        # 格式化性格简述
        personality = custom_role_model.personality
        if personality != None and personality != '':
            personality = PERSONALITY_PROMPT.format(
                role_name=role_name, personality=personality)
        else:
            personality = ""

        # 格式化情景简述
        scenario = custom_role_model.scenario
        if scenario != None and scenario != '':
            scenario = SCENARIO_PROMPT.format(scenario=scenario)
        else:
            scenario = ""

        # Generate the prompt to be sent to the language model
        prompt = PROMPT.format(
            role_name=role_name, persona=persona, first_message=first_message, personality=personality,
            scenario=scenario, examples_of_dialogue=examples_of_dialogue, you_name=you_name,
            long_history=long_history, short_history=short_history, input=input
        )

        return prompt
