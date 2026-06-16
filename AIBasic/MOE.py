import torch
import torch.nn as nn
import torch.nn.functional as F

class BasicExpert(nn.Module):
    def __init__(self, feature_in, feature_out):
        super().__init__()
        self.fc = nn.Linear(feature_in, feature_out)

    def forward(self, x):
        return self.fc(x)

class BasicMOE(nn.Module):
    def __init__(self, feature_in, feature_out, num_experts):
        super().__init__()
        self.gate = nn.Linear(feature_in, num_experts)
        # output shape (batch_size, num_experts)
        self.experts = nn.ModuleList(
            BasicExpert(
                feature_in, feature_out
            ) for _ in range(num_experts)
        )

    def forward(self, x):
        # x shape (batch, feature_in)
        # feature_in also calls hidden_size/hidden_dim
        expert_weights = self.gate(x)
        expert_out_list = [
            expert(x) for expert in self.experts
        ] # for each expert, output (batch, feature_in)

        expert_outs = [
            expert_out.unsqueeze(1)
            for expert_out in expert_out_list
        ]

        # expert_out (batch, 1, feature_out)
        expert_out = torch.concat(
            expert_outs,
            dim = 1
        )
        # expert_output shape (b, num_experts, feature_out)

        # expert_weights
        expert_weights = F.softmax(expert_weights, dim=1)
        # (batch, num_experts)

        expert_weights = expert_weights.unsqueeze(1)
        # (batch, 1, num_experts)
        output = expert_weights @ expert_out # (batch, feature_out)
        
        return output.squeeze(1)
    
def test_basic_moe():
    x = torch.rand(4, 512)
    basic_moe = BasicMOE(512, 128, 4)
    output = basic_moe(x)
    print(output.shape)

test_basic_moe()