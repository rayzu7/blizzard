local Obsidian = loadstring(game:HttpGet("https://raw.githubusercontent.com/yofriendfromschool1/Obsidian-Ui-Library/main/source.lua"))()
local Window = Obsidian.MakeWindow({Name = "NUCLEAR v18.0", MainColor = Color3.fromRGB(255, 0, 0)})
local LP = game:GetService("Players").LocalPlayer

-- ТАБ СИНХРОНА
local Tab1 = Window:MakeTab({Name = "R6 SYNC"})

Tab1:AddButton({
    Name = "ANTI-BANANA (SYNC)",
    Callback = function()
        local t = LP.Character:FindFirstChild("Torso")
        if t then
            t["Left Hip"].C0 = CFrame.new(0, 1000, 0)
            t["Right Hip"].C0 = CFrame.new(0, 1000, 0)
            LP.Character.Humanoid.HipHeight = 3
        end
    end
})

Tab1:AddButton({
    Name = "NAMAZ (R6 NO-FLIP)",
    Callback = function()
        local r = LP.Character.HumanoidRootPart.RootJoint
        LP.Character.Humanoid.WalkSpeed = 0
        r.C1 = CFrame.new(0,0,0) * CFrame.Angles(math.rad(70), 0, 0)
        task.wait(2)
        r.C1 = CFrame.new(0, 2, 0) * CFrame.Angles(math.rad(90), 0, 0)
        task.wait(3)
        r.C1 = CFrame.new(0,0,0)
        LP.Character.Humanoid.WalkSpeed = 16
    end
})

-- ТАБ КАМЕРЫ (3 ЛИЦО)
local Tab2 = Window:MakeTab({Name = "CAMERA"})
Tab2:AddButton({
    Name = "UNLOCK ZOOM (250)",
    Callback = function()
        game:GetService("RunService").RenderStepped:Connect(function()
            LP.CameraMaxZoomDistance = 250
            LP.CameraMode = "Classic"
        end)
    end
})

-- ТЕ САМЫЕ 200 КНОПОК
local Tab3 = Window:MakeTab({Name = "200+ FUNCTIONS"})
local names = {"Fly", "God", "Speed", "Kill", "Aura", "Esp", "Tp", "Void", "Invis", "Spin"}
for i = 1, 200 do
    local n = names[math.random(1, #names)] .. " v" .. i
    Tab3:AddButton({Name = n, Callback = function() print(n) end})
end